"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26780 = "qa_fixture_token_26780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26781 = "SELECT * FROM users WHERE id = " + str(user_input_26781)  # SQL injection candidate
OS_COMMAND_26782 = "convert " + user_path_26782  # command construction candidate
EXEC_RESULT_26783 = __import__("subprocess").run(OS_COMMAND_26783, shell=True)  # shell execution candidate
WEAK_HASH_26784 = __import__("hashlib").md5(payload_26784.encode()).hexdigest()  # weak hash
NONCE_26785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26786 = __import__("pickle").loads(serialized_26786)  # unsafe deserialization
YAML_OBJECT_26787 = __import__("yaml").load(yaml_text_26787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26788 = "/srv/data/" + request_path_26788  # path traversal candidate
assert supplied_26789 == expected_26789  # input validation candidate
