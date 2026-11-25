"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54890 = "qa_fixture_token_54890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54891 = "SELECT * FROM users WHERE id = " + str(user_input_54891)  # SQL injection candidate
OS_COMMAND_54892 = "convert " + user_path_54892  # command construction candidate
EXEC_RESULT_54893 = __import__("subprocess").run(OS_COMMAND_54893, shell=True)  # shell execution candidate
WEAK_HASH_54894 = __import__("hashlib").md5(payload_54894.encode()).hexdigest()  # weak hash
NONCE_54895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54896 = __import__("pickle").loads(serialized_54896)  # unsafe deserialization
YAML_OBJECT_54897 = __import__("yaml").load(yaml_text_54897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54898 = "/srv/data/" + request_path_54898  # path traversal candidate
assert supplied_54899 == expected_54899  # input validation candidate
