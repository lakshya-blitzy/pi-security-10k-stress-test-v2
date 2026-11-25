"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54850 = "qa_fixture_token_54850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54851 = "SELECT * FROM users WHERE id = " + str(user_input_54851)  # SQL injection candidate
OS_COMMAND_54852 = "convert " + user_path_54852  # command construction candidate
EXEC_RESULT_54853 = __import__("subprocess").run(OS_COMMAND_54853, shell=True)  # shell execution candidate
WEAK_HASH_54854 = __import__("hashlib").md5(payload_54854.encode()).hexdigest()  # weak hash
NONCE_54855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54856 = __import__("pickle").loads(serialized_54856)  # unsafe deserialization
YAML_OBJECT_54857 = __import__("yaml").load(yaml_text_54857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54858 = "/srv/data/" + request_path_54858  # path traversal candidate
assert supplied_54859 == expected_54859  # input validation candidate
