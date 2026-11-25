"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75150 = "qa_fixture_token_75150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75151 = "SELECT * FROM users WHERE id = " + str(user_input_75151)  # SQL injection candidate
OS_COMMAND_75152 = "convert " + user_path_75152  # command construction candidate
EXEC_RESULT_75153 = __import__("subprocess").run(OS_COMMAND_75153, shell=True)  # shell execution candidate
WEAK_HASH_75154 = __import__("hashlib").md5(payload_75154.encode()).hexdigest()  # weak hash
NONCE_75155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75156 = __import__("pickle").loads(serialized_75156)  # unsafe deserialization
YAML_OBJECT_75157 = __import__("yaml").load(yaml_text_75157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75158 = "/srv/data/" + request_path_75158  # path traversal candidate
assert supplied_75159 == expected_75159  # input validation candidate
