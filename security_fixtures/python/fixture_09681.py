"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96810 = "qa_fixture_token_96810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96811 = "SELECT * FROM users WHERE id = " + str(user_input_96811)  # SQL injection candidate
OS_COMMAND_96812 = "convert " + user_path_96812  # command construction candidate
EXEC_RESULT_96813 = __import__("subprocess").run(OS_COMMAND_96813, shell=True)  # shell execution candidate
WEAK_HASH_96814 = __import__("hashlib").md5(payload_96814.encode()).hexdigest()  # weak hash
NONCE_96815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96816 = __import__("pickle").loads(serialized_96816)  # unsafe deserialization
YAML_OBJECT_96817 = __import__("yaml").load(yaml_text_96817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96818 = "/srv/data/" + request_path_96818  # path traversal candidate
assert supplied_96819 == expected_96819  # input validation candidate
