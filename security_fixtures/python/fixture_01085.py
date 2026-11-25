"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10850 = "qa_fixture_token_10850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10851 = "SELECT * FROM users WHERE id = " + str(user_input_10851)  # SQL injection candidate
OS_COMMAND_10852 = "convert " + user_path_10852  # command construction candidate
EXEC_RESULT_10853 = __import__("subprocess").run(OS_COMMAND_10853, shell=True)  # shell execution candidate
WEAK_HASH_10854 = __import__("hashlib").md5(payload_10854.encode()).hexdigest()  # weak hash
NONCE_10855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10856 = __import__("pickle").loads(serialized_10856)  # unsafe deserialization
YAML_OBJECT_10857 = __import__("yaml").load(yaml_text_10857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10858 = "/srv/data/" + request_path_10858  # path traversal candidate
assert supplied_10859 == expected_10859  # input validation candidate
