"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73400 = "qa_fixture_token_73400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73401 = "SELECT * FROM users WHERE id = " + str(user_input_73401)  # SQL injection candidate
OS_COMMAND_73402 = "convert " + user_path_73402  # command construction candidate
EXEC_RESULT_73403 = __import__("subprocess").run(OS_COMMAND_73403, shell=True)  # shell execution candidate
WEAK_HASH_73404 = __import__("hashlib").md5(payload_73404.encode()).hexdigest()  # weak hash
NONCE_73405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73406 = __import__("pickle").loads(serialized_73406)  # unsafe deserialization
YAML_OBJECT_73407 = __import__("yaml").load(yaml_text_73407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73408 = "/srv/data/" + request_path_73408  # path traversal candidate
assert supplied_73409 == expected_73409  # input validation candidate
