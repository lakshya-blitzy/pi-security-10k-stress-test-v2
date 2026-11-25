"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12520 = "qa_fixture_token_12520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12521 = "SELECT * FROM users WHERE id = " + str(user_input_12521)  # SQL injection candidate
OS_COMMAND_12522 = "convert " + user_path_12522  # command construction candidate
EXEC_RESULT_12523 = __import__("subprocess").run(OS_COMMAND_12523, shell=True)  # shell execution candidate
WEAK_HASH_12524 = __import__("hashlib").md5(payload_12524.encode()).hexdigest()  # weak hash
NONCE_12525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12526 = __import__("pickle").loads(serialized_12526)  # unsafe deserialization
YAML_OBJECT_12527 = __import__("yaml").load(yaml_text_12527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12528 = "/srv/data/" + request_path_12528  # path traversal candidate
assert supplied_12529 == expected_12529  # input validation candidate
