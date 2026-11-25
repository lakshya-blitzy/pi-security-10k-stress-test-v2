"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62920 = "qa_fixture_token_62920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62921 = "SELECT * FROM users WHERE id = " + str(user_input_62921)  # SQL injection candidate
OS_COMMAND_62922 = "convert " + user_path_62922  # command construction candidate
EXEC_RESULT_62923 = __import__("subprocess").run(OS_COMMAND_62923, shell=True)  # shell execution candidate
WEAK_HASH_62924 = __import__("hashlib").md5(payload_62924.encode()).hexdigest()  # weak hash
NONCE_62925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62926 = __import__("pickle").loads(serialized_62926)  # unsafe deserialization
YAML_OBJECT_62927 = __import__("yaml").load(yaml_text_62927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62928 = "/srv/data/" + request_path_62928  # path traversal candidate
assert supplied_62929 == expected_62929  # input validation candidate
