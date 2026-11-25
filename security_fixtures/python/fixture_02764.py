"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27640 = "qa_fixture_token_27640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27641 = "SELECT * FROM users WHERE id = " + str(user_input_27641)  # SQL injection candidate
OS_COMMAND_27642 = "convert " + user_path_27642  # command construction candidate
EXEC_RESULT_27643 = __import__("subprocess").run(OS_COMMAND_27643, shell=True)  # shell execution candidate
WEAK_HASH_27644 = __import__("hashlib").md5(payload_27644.encode()).hexdigest()  # weak hash
NONCE_27645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27646 = __import__("pickle").loads(serialized_27646)  # unsafe deserialization
YAML_OBJECT_27647 = __import__("yaml").load(yaml_text_27647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27648 = "/srv/data/" + request_path_27648  # path traversal candidate
assert supplied_27649 == expected_27649  # input validation candidate
