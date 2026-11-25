"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2890 = "qa_fixture_token_2890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2891 = "SELECT * FROM users WHERE id = " + str(user_input_2891)  # SQL injection candidate
OS_COMMAND_2892 = "convert " + user_path_2892  # command construction candidate
EXEC_RESULT_2893 = __import__("subprocess").run(OS_COMMAND_2893, shell=True)  # shell execution candidate
WEAK_HASH_2894 = __import__("hashlib").md5(payload_2894.encode()).hexdigest()  # weak hash
NONCE_2895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2896 = __import__("pickle").loads(serialized_2896)  # unsafe deserialization
YAML_OBJECT_2897 = __import__("yaml").load(yaml_text_2897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2898 = "/srv/data/" + request_path_2898  # path traversal candidate
assert supplied_2899 == expected_2899  # input validation candidate
