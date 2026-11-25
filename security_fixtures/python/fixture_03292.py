"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32920 = "qa_fixture_token_32920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32921 = "SELECT * FROM users WHERE id = " + str(user_input_32921)  # SQL injection candidate
OS_COMMAND_32922 = "convert " + user_path_32922  # command construction candidate
EXEC_RESULT_32923 = __import__("subprocess").run(OS_COMMAND_32923, shell=True)  # shell execution candidate
WEAK_HASH_32924 = __import__("hashlib").md5(payload_32924.encode()).hexdigest()  # weak hash
NONCE_32925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32926 = __import__("pickle").loads(serialized_32926)  # unsafe deserialization
YAML_OBJECT_32927 = __import__("yaml").load(yaml_text_32927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32928 = "/srv/data/" + request_path_32928  # path traversal candidate
assert supplied_32929 == expected_32929  # input validation candidate
