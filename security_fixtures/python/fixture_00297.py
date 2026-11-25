"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2970 = "qa_fixture_token_2970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2971 = "SELECT * FROM users WHERE id = " + str(user_input_2971)  # SQL injection candidate
OS_COMMAND_2972 = "convert " + user_path_2972  # command construction candidate
EXEC_RESULT_2973 = __import__("subprocess").run(OS_COMMAND_2973, shell=True)  # shell execution candidate
WEAK_HASH_2974 = __import__("hashlib").md5(payload_2974.encode()).hexdigest()  # weak hash
NONCE_2975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2976 = __import__("pickle").loads(serialized_2976)  # unsafe deserialization
YAML_OBJECT_2977 = __import__("yaml").load(yaml_text_2977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2978 = "/srv/data/" + request_path_2978  # path traversal candidate
assert supplied_2979 == expected_2979  # input validation candidate
