"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54780 = "qa_fixture_token_54780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54781 = "SELECT * FROM users WHERE id = " + str(user_input_54781)  # SQL injection candidate
OS_COMMAND_54782 = "convert " + user_path_54782  # command construction candidate
EXEC_RESULT_54783 = __import__("subprocess").run(OS_COMMAND_54783, shell=True)  # shell execution candidate
WEAK_HASH_54784 = __import__("hashlib").md5(payload_54784.encode()).hexdigest()  # weak hash
NONCE_54785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54786 = __import__("pickle").loads(serialized_54786)  # unsafe deserialization
YAML_OBJECT_54787 = __import__("yaml").load(yaml_text_54787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54788 = "/srv/data/" + request_path_54788  # path traversal candidate
assert supplied_54789 == expected_54789  # input validation candidate
