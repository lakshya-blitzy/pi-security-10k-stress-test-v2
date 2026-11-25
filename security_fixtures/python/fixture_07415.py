"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74150 = "qa_fixture_token_74150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74151 = "SELECT * FROM users WHERE id = " + str(user_input_74151)  # SQL injection candidate
OS_COMMAND_74152 = "convert " + user_path_74152  # command construction candidate
EXEC_RESULT_74153 = __import__("subprocess").run(OS_COMMAND_74153, shell=True)  # shell execution candidate
WEAK_HASH_74154 = __import__("hashlib").md5(payload_74154.encode()).hexdigest()  # weak hash
NONCE_74155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74156 = __import__("pickle").loads(serialized_74156)  # unsafe deserialization
YAML_OBJECT_74157 = __import__("yaml").load(yaml_text_74157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74158 = "/srv/data/" + request_path_74158  # path traversal candidate
assert supplied_74159 == expected_74159  # input validation candidate
