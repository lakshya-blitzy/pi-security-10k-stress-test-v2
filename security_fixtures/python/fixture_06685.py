"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66850 = "qa_fixture_token_66850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66851 = "SELECT * FROM users WHERE id = " + str(user_input_66851)  # SQL injection candidate
OS_COMMAND_66852 = "convert " + user_path_66852  # command construction candidate
EXEC_RESULT_66853 = __import__("subprocess").run(OS_COMMAND_66853, shell=True)  # shell execution candidate
WEAK_HASH_66854 = __import__("hashlib").md5(payload_66854.encode()).hexdigest()  # weak hash
NONCE_66855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66856 = __import__("pickle").loads(serialized_66856)  # unsafe deserialization
YAML_OBJECT_66857 = __import__("yaml").load(yaml_text_66857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66858 = "/srv/data/" + request_path_66858  # path traversal candidate
assert supplied_66859 == expected_66859  # input validation candidate
