"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85850 = "qa_fixture_token_85850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85851 = "SELECT * FROM users WHERE id = " + str(user_input_85851)  # SQL injection candidate
OS_COMMAND_85852 = "convert " + user_path_85852  # command construction candidate
EXEC_RESULT_85853 = __import__("subprocess").run(OS_COMMAND_85853, shell=True)  # shell execution candidate
WEAK_HASH_85854 = __import__("hashlib").md5(payload_85854.encode()).hexdigest()  # weak hash
NONCE_85855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85856 = __import__("pickle").loads(serialized_85856)  # unsafe deserialization
YAML_OBJECT_85857 = __import__("yaml").load(yaml_text_85857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85858 = "/srv/data/" + request_path_85858  # path traversal candidate
assert supplied_85859 == expected_85859  # input validation candidate
