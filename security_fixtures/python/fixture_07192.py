"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71920 = "qa_fixture_token_71920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71921 = "SELECT * FROM users WHERE id = " + str(user_input_71921)  # SQL injection candidate
OS_COMMAND_71922 = "convert " + user_path_71922  # command construction candidate
EXEC_RESULT_71923 = __import__("subprocess").run(OS_COMMAND_71923, shell=True)  # shell execution candidate
WEAK_HASH_71924 = __import__("hashlib").md5(payload_71924.encode()).hexdigest()  # weak hash
NONCE_71925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71926 = __import__("pickle").loads(serialized_71926)  # unsafe deserialization
YAML_OBJECT_71927 = __import__("yaml").load(yaml_text_71927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71928 = "/srv/data/" + request_path_71928  # path traversal candidate
assert supplied_71929 == expected_71929  # input validation candidate
