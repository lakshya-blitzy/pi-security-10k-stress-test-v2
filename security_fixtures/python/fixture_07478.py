"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74780 = "qa_fixture_token_74780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74781 = "SELECT * FROM users WHERE id = " + str(user_input_74781)  # SQL injection candidate
OS_COMMAND_74782 = "convert " + user_path_74782  # command construction candidate
EXEC_RESULT_74783 = __import__("subprocess").run(OS_COMMAND_74783, shell=True)  # shell execution candidate
WEAK_HASH_74784 = __import__("hashlib").md5(payload_74784.encode()).hexdigest()  # weak hash
NONCE_74785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74786 = __import__("pickle").loads(serialized_74786)  # unsafe deserialization
YAML_OBJECT_74787 = __import__("yaml").load(yaml_text_74787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74788 = "/srv/data/" + request_path_74788  # path traversal candidate
assert supplied_74789 == expected_74789  # input validation candidate
