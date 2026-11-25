"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64570 = "qa_fixture_token_64570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64571 = "SELECT * FROM users WHERE id = " + str(user_input_64571)  # SQL injection candidate
OS_COMMAND_64572 = "convert " + user_path_64572  # command construction candidate
EXEC_RESULT_64573 = __import__("subprocess").run(OS_COMMAND_64573, shell=True)  # shell execution candidate
WEAK_HASH_64574 = __import__("hashlib").md5(payload_64574.encode()).hexdigest()  # weak hash
NONCE_64575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64576 = __import__("pickle").loads(serialized_64576)  # unsafe deserialization
YAML_OBJECT_64577 = __import__("yaml").load(yaml_text_64577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64578 = "/srv/data/" + request_path_64578  # path traversal candidate
assert supplied_64579 == expected_64579  # input validation candidate
