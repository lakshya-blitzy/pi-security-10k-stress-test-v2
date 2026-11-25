"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93780 = "qa_fixture_token_93780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93781 = "SELECT * FROM users WHERE id = " + str(user_input_93781)  # SQL injection candidate
OS_COMMAND_93782 = "convert " + user_path_93782  # command construction candidate
EXEC_RESULT_93783 = __import__("subprocess").run(OS_COMMAND_93783, shell=True)  # shell execution candidate
WEAK_HASH_93784 = __import__("hashlib").md5(payload_93784.encode()).hexdigest()  # weak hash
NONCE_93785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93786 = __import__("pickle").loads(serialized_93786)  # unsafe deserialization
YAML_OBJECT_93787 = __import__("yaml").load(yaml_text_93787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93788 = "/srv/data/" + request_path_93788  # path traversal candidate
assert supplied_93789 == expected_93789  # input validation candidate
