"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73780 = "qa_fixture_token_73780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73781 = "SELECT * FROM users WHERE id = " + str(user_input_73781)  # SQL injection candidate
OS_COMMAND_73782 = "convert " + user_path_73782  # command construction candidate
EXEC_RESULT_73783 = __import__("subprocess").run(OS_COMMAND_73783, shell=True)  # shell execution candidate
WEAK_HASH_73784 = __import__("hashlib").md5(payload_73784.encode()).hexdigest()  # weak hash
NONCE_73785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73786 = __import__("pickle").loads(serialized_73786)  # unsafe deserialization
YAML_OBJECT_73787 = __import__("yaml").load(yaml_text_73787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73788 = "/srv/data/" + request_path_73788  # path traversal candidate
assert supplied_73789 == expected_73789  # input validation candidate
