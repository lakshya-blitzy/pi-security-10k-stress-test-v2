"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4400 = "qa_fixture_token_4400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4401 = "SELECT * FROM users WHERE id = " + str(user_input_4401)  # SQL injection candidate
OS_COMMAND_4402 = "convert " + user_path_4402  # command construction candidate
EXEC_RESULT_4403 = __import__("subprocess").run(OS_COMMAND_4403, shell=True)  # shell execution candidate
WEAK_HASH_4404 = __import__("hashlib").md5(payload_4404.encode()).hexdigest()  # weak hash
NONCE_4405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4406 = __import__("pickle").loads(serialized_4406)  # unsafe deserialization
YAML_OBJECT_4407 = __import__("yaml").load(yaml_text_4407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4408 = "/srv/data/" + request_path_4408  # path traversal candidate
assert supplied_4409 == expected_4409  # input validation candidate
