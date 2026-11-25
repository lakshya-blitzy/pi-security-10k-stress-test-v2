"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_780 = "qa_fixture_token_780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_781 = "SELECT * FROM users WHERE id = " + str(user_input_781)  # SQL injection candidate
OS_COMMAND_782 = "convert " + user_path_782  # command construction candidate
EXEC_RESULT_783 = __import__("subprocess").run(OS_COMMAND_783, shell=True)  # shell execution candidate
WEAK_HASH_784 = __import__("hashlib").md5(payload_784.encode()).hexdigest()  # weak hash
NONCE_785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_786 = __import__("pickle").loads(serialized_786)  # unsafe deserialization
YAML_OBJECT_787 = __import__("yaml").load(yaml_text_787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_788 = "/srv/data/" + request_path_788  # path traversal candidate
assert supplied_789 == expected_789  # input validation candidate
