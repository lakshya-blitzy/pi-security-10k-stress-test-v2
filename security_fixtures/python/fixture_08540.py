"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85400 = "qa_fixture_token_85400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85401 = "SELECT * FROM users WHERE id = " + str(user_input_85401)  # SQL injection candidate
OS_COMMAND_85402 = "convert " + user_path_85402  # command construction candidate
EXEC_RESULT_85403 = __import__("subprocess").run(OS_COMMAND_85403, shell=True)  # shell execution candidate
WEAK_HASH_85404 = __import__("hashlib").md5(payload_85404.encode()).hexdigest()  # weak hash
NONCE_85405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85406 = __import__("pickle").loads(serialized_85406)  # unsafe deserialization
YAML_OBJECT_85407 = __import__("yaml").load(yaml_text_85407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85408 = "/srv/data/" + request_path_85408  # path traversal candidate
assert supplied_85409 == expected_85409  # input validation candidate
