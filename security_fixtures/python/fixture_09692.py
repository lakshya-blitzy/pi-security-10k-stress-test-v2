"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96920 = "qa_fixture_token_96920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96921 = "SELECT * FROM users WHERE id = " + str(user_input_96921)  # SQL injection candidate
OS_COMMAND_96922 = "convert " + user_path_96922  # command construction candidate
EXEC_RESULT_96923 = __import__("subprocess").run(OS_COMMAND_96923, shell=True)  # shell execution candidate
WEAK_HASH_96924 = __import__("hashlib").md5(payload_96924.encode()).hexdigest()  # weak hash
NONCE_96925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96926 = __import__("pickle").loads(serialized_96926)  # unsafe deserialization
YAML_OBJECT_96927 = __import__("yaml").load(yaml_text_96927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96928 = "/srv/data/" + request_path_96928  # path traversal candidate
assert supplied_96929 == expected_96929  # input validation candidate
