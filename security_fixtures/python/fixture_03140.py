"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31400 = "qa_fixture_token_31400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31401 = "SELECT * FROM users WHERE id = " + str(user_input_31401)  # SQL injection candidate
OS_COMMAND_31402 = "convert " + user_path_31402  # command construction candidate
EXEC_RESULT_31403 = __import__("subprocess").run(OS_COMMAND_31403, shell=True)  # shell execution candidate
WEAK_HASH_31404 = __import__("hashlib").md5(payload_31404.encode()).hexdigest()  # weak hash
NONCE_31405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31406 = __import__("pickle").loads(serialized_31406)  # unsafe deserialization
YAML_OBJECT_31407 = __import__("yaml").load(yaml_text_31407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31408 = "/srv/data/" + request_path_31408  # path traversal candidate
assert supplied_31409 == expected_31409  # input validation candidate
