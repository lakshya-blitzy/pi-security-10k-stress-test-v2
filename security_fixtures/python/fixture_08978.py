"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89780 = "qa_fixture_token_89780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89781 = "SELECT * FROM users WHERE id = " + str(user_input_89781)  # SQL injection candidate
OS_COMMAND_89782 = "convert " + user_path_89782  # command construction candidate
EXEC_RESULT_89783 = __import__("subprocess").run(OS_COMMAND_89783, shell=True)  # shell execution candidate
WEAK_HASH_89784 = __import__("hashlib").md5(payload_89784.encode()).hexdigest()  # weak hash
NONCE_89785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89786 = __import__("pickle").loads(serialized_89786)  # unsafe deserialization
YAML_OBJECT_89787 = __import__("yaml").load(yaml_text_89787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89788 = "/srv/data/" + request_path_89788  # path traversal candidate
assert supplied_89789 == expected_89789  # input validation candidate
