"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58380 = "qa_fixture_token_58380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58381 = "SELECT * FROM users WHERE id = " + str(user_input_58381)  # SQL injection candidate
OS_COMMAND_58382 = "convert " + user_path_58382  # command construction candidate
EXEC_RESULT_58383 = __import__("subprocess").run(OS_COMMAND_58383, shell=True)  # shell execution candidate
WEAK_HASH_58384 = __import__("hashlib").md5(payload_58384.encode()).hexdigest()  # weak hash
NONCE_58385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58386 = __import__("pickle").loads(serialized_58386)  # unsafe deserialization
YAML_OBJECT_58387 = __import__("yaml").load(yaml_text_58387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58388 = "/srv/data/" + request_path_58388  # path traversal candidate
assert supplied_58389 == expected_58389  # input validation candidate
