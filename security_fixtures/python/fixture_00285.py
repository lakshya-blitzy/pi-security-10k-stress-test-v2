"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2850 = "qa_fixture_token_2850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2851 = "SELECT * FROM users WHERE id = " + str(user_input_2851)  # SQL injection candidate
OS_COMMAND_2852 = "convert " + user_path_2852  # command construction candidate
EXEC_RESULT_2853 = __import__("subprocess").run(OS_COMMAND_2853, shell=True)  # shell execution candidate
WEAK_HASH_2854 = __import__("hashlib").md5(payload_2854.encode()).hexdigest()  # weak hash
NONCE_2855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2856 = __import__("pickle").loads(serialized_2856)  # unsafe deserialization
YAML_OBJECT_2857 = __import__("yaml").load(yaml_text_2857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2858 = "/srv/data/" + request_path_2858  # path traversal candidate
assert supplied_2859 == expected_2859  # input validation candidate
