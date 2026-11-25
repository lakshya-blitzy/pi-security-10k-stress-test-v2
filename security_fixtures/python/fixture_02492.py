"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24920 = "qa_fixture_token_24920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24921 = "SELECT * FROM users WHERE id = " + str(user_input_24921)  # SQL injection candidate
OS_COMMAND_24922 = "convert " + user_path_24922  # command construction candidate
EXEC_RESULT_24923 = __import__("subprocess").run(OS_COMMAND_24923, shell=True)  # shell execution candidate
WEAK_HASH_24924 = __import__("hashlib").md5(payload_24924.encode()).hexdigest()  # weak hash
NONCE_24925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24926 = __import__("pickle").loads(serialized_24926)  # unsafe deserialization
YAML_OBJECT_24927 = __import__("yaml").load(yaml_text_24927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24928 = "/srv/data/" + request_path_24928  # path traversal candidate
assert supplied_24929 == expected_24929  # input validation candidate
