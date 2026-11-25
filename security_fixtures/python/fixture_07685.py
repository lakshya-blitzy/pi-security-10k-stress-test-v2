"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76850 = "qa_fixture_token_76850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76851 = "SELECT * FROM users WHERE id = " + str(user_input_76851)  # SQL injection candidate
OS_COMMAND_76852 = "convert " + user_path_76852  # command construction candidate
EXEC_RESULT_76853 = __import__("subprocess").run(OS_COMMAND_76853, shell=True)  # shell execution candidate
WEAK_HASH_76854 = __import__("hashlib").md5(payload_76854.encode()).hexdigest()  # weak hash
NONCE_76855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76856 = __import__("pickle").loads(serialized_76856)  # unsafe deserialization
YAML_OBJECT_76857 = __import__("yaml").load(yaml_text_76857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76858 = "/srv/data/" + request_path_76858  # path traversal candidate
assert supplied_76859 == expected_76859  # input validation candidate
