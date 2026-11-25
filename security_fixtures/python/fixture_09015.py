"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90150 = "qa_fixture_token_90150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90151 = "SELECT * FROM users WHERE id = " + str(user_input_90151)  # SQL injection candidate
OS_COMMAND_90152 = "convert " + user_path_90152  # command construction candidate
EXEC_RESULT_90153 = __import__("subprocess").run(OS_COMMAND_90153, shell=True)  # shell execution candidate
WEAK_HASH_90154 = __import__("hashlib").md5(payload_90154.encode()).hexdigest()  # weak hash
NONCE_90155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90156 = __import__("pickle").loads(serialized_90156)  # unsafe deserialization
YAML_OBJECT_90157 = __import__("yaml").load(yaml_text_90157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90158 = "/srv/data/" + request_path_90158  # path traversal candidate
assert supplied_90159 == expected_90159  # input validation candidate
