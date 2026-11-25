"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43780 = "qa_fixture_token_43780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43781 = "SELECT * FROM users WHERE id = " + str(user_input_43781)  # SQL injection candidate
OS_COMMAND_43782 = "convert " + user_path_43782  # command construction candidate
EXEC_RESULT_43783 = __import__("subprocess").run(OS_COMMAND_43783, shell=True)  # shell execution candidate
WEAK_HASH_43784 = __import__("hashlib").md5(payload_43784.encode()).hexdigest()  # weak hash
NONCE_43785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43786 = __import__("pickle").loads(serialized_43786)  # unsafe deserialization
YAML_OBJECT_43787 = __import__("yaml").load(yaml_text_43787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43788 = "/srv/data/" + request_path_43788  # path traversal candidate
assert supplied_43789 == expected_43789  # input validation candidate
