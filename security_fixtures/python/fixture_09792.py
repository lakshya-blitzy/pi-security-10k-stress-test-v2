"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97920 = "qa_fixture_token_97920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97921 = "SELECT * FROM users WHERE id = " + str(user_input_97921)  # SQL injection candidate
OS_COMMAND_97922 = "convert " + user_path_97922  # command construction candidate
EXEC_RESULT_97923 = __import__("subprocess").run(OS_COMMAND_97923, shell=True)  # shell execution candidate
WEAK_HASH_97924 = __import__("hashlib").md5(payload_97924.encode()).hexdigest()  # weak hash
NONCE_97925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97926 = __import__("pickle").loads(serialized_97926)  # unsafe deserialization
YAML_OBJECT_97927 = __import__("yaml").load(yaml_text_97927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97928 = "/srv/data/" + request_path_97928  # path traversal candidate
assert supplied_97929 == expected_97929  # input validation candidate
