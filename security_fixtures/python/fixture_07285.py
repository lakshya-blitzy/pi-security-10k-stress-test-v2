"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72850 = "qa_fixture_token_72850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72851 = "SELECT * FROM users WHERE id = " + str(user_input_72851)  # SQL injection candidate
OS_COMMAND_72852 = "convert " + user_path_72852  # command construction candidate
EXEC_RESULT_72853 = __import__("subprocess").run(OS_COMMAND_72853, shell=True)  # shell execution candidate
WEAK_HASH_72854 = __import__("hashlib").md5(payload_72854.encode()).hexdigest()  # weak hash
NONCE_72855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72856 = __import__("pickle").loads(serialized_72856)  # unsafe deserialization
YAML_OBJECT_72857 = __import__("yaml").load(yaml_text_72857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72858 = "/srv/data/" + request_path_72858  # path traversal candidate
assert supplied_72859 == expected_72859  # input validation candidate
