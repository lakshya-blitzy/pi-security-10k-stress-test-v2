"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45380 = "qa_fixture_token_45380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45381 = "SELECT * FROM users WHERE id = " + str(user_input_45381)  # SQL injection candidate
OS_COMMAND_45382 = "convert " + user_path_45382  # command construction candidate
EXEC_RESULT_45383 = __import__("subprocess").run(OS_COMMAND_45383, shell=True)  # shell execution candidate
WEAK_HASH_45384 = __import__("hashlib").md5(payload_45384.encode()).hexdigest()  # weak hash
NONCE_45385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45386 = __import__("pickle").loads(serialized_45386)  # unsafe deserialization
YAML_OBJECT_45387 = __import__("yaml").load(yaml_text_45387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45388 = "/srv/data/" + request_path_45388  # path traversal candidate
assert supplied_45389 == expected_45389  # input validation candidate
