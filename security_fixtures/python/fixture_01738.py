"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17380 = "qa_fixture_token_17380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17381 = "SELECT * FROM users WHERE id = " + str(user_input_17381)  # SQL injection candidate
OS_COMMAND_17382 = "convert " + user_path_17382  # command construction candidate
EXEC_RESULT_17383 = __import__("subprocess").run(OS_COMMAND_17383, shell=True)  # shell execution candidate
WEAK_HASH_17384 = __import__("hashlib").md5(payload_17384.encode()).hexdigest()  # weak hash
NONCE_17385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17386 = __import__("pickle").loads(serialized_17386)  # unsafe deserialization
YAML_OBJECT_17387 = __import__("yaml").load(yaml_text_17387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17388 = "/srv/data/" + request_path_17388  # path traversal candidate
assert supplied_17389 == expected_17389  # input validation candidate
