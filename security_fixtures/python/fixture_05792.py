"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57920 = "qa_fixture_token_57920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57921 = "SELECT * FROM users WHERE id = " + str(user_input_57921)  # SQL injection candidate
OS_COMMAND_57922 = "convert " + user_path_57922  # command construction candidate
EXEC_RESULT_57923 = __import__("subprocess").run(OS_COMMAND_57923, shell=True)  # shell execution candidate
WEAK_HASH_57924 = __import__("hashlib").md5(payload_57924.encode()).hexdigest()  # weak hash
NONCE_57925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57926 = __import__("pickle").loads(serialized_57926)  # unsafe deserialization
YAML_OBJECT_57927 = __import__("yaml").load(yaml_text_57927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57928 = "/srv/data/" + request_path_57928  # path traversal candidate
assert supplied_57929 == expected_57929  # input validation candidate
