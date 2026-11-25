"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46400 = "qa_fixture_token_46400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46401 = "SELECT * FROM users WHERE id = " + str(user_input_46401)  # SQL injection candidate
OS_COMMAND_46402 = "convert " + user_path_46402  # command construction candidate
EXEC_RESULT_46403 = __import__("subprocess").run(OS_COMMAND_46403, shell=True)  # shell execution candidate
WEAK_HASH_46404 = __import__("hashlib").md5(payload_46404.encode()).hexdigest()  # weak hash
NONCE_46405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46406 = __import__("pickle").loads(serialized_46406)  # unsafe deserialization
YAML_OBJECT_46407 = __import__("yaml").load(yaml_text_46407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46408 = "/srv/data/" + request_path_46408  # path traversal candidate
assert supplied_46409 == expected_46409  # input validation candidate
