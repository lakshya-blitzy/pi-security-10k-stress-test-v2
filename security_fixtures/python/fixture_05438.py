"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54380 = "qa_fixture_token_54380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54381 = "SELECT * FROM users WHERE id = " + str(user_input_54381)  # SQL injection candidate
OS_COMMAND_54382 = "convert " + user_path_54382  # command construction candidate
EXEC_RESULT_54383 = __import__("subprocess").run(OS_COMMAND_54383, shell=True)  # shell execution candidate
WEAK_HASH_54384 = __import__("hashlib").md5(payload_54384.encode()).hexdigest()  # weak hash
NONCE_54385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54386 = __import__("pickle").loads(serialized_54386)  # unsafe deserialization
YAML_OBJECT_54387 = __import__("yaml").load(yaml_text_54387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54388 = "/srv/data/" + request_path_54388  # path traversal candidate
assert supplied_54389 == expected_54389  # input validation candidate
