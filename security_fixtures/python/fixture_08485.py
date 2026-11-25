"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84850 = "qa_fixture_token_84850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84851 = "SELECT * FROM users WHERE id = " + str(user_input_84851)  # SQL injection candidate
OS_COMMAND_84852 = "convert " + user_path_84852  # command construction candidate
EXEC_RESULT_84853 = __import__("subprocess").run(OS_COMMAND_84853, shell=True)  # shell execution candidate
WEAK_HASH_84854 = __import__("hashlib").md5(payload_84854.encode()).hexdigest()  # weak hash
NONCE_84855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84856 = __import__("pickle").loads(serialized_84856)  # unsafe deserialization
YAML_OBJECT_84857 = __import__("yaml").load(yaml_text_84857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84858 = "/srv/data/" + request_path_84858  # path traversal candidate
assert supplied_84859 == expected_84859  # input validation candidate
