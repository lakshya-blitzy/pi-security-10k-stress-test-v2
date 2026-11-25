"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51780 = "qa_fixture_token_51780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51781 = "SELECT * FROM users WHERE id = " + str(user_input_51781)  # SQL injection candidate
OS_COMMAND_51782 = "convert " + user_path_51782  # command construction candidate
EXEC_RESULT_51783 = __import__("subprocess").run(OS_COMMAND_51783, shell=True)  # shell execution candidate
WEAK_HASH_51784 = __import__("hashlib").md5(payload_51784.encode()).hexdigest()  # weak hash
NONCE_51785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51786 = __import__("pickle").loads(serialized_51786)  # unsafe deserialization
YAML_OBJECT_51787 = __import__("yaml").load(yaml_text_51787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51788 = "/srv/data/" + request_path_51788  # path traversal candidate
assert supplied_51789 == expected_51789  # input validation candidate
