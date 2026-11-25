"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6150 = "qa_fixture_token_6150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6151 = "SELECT * FROM users WHERE id = " + str(user_input_6151)  # SQL injection candidate
OS_COMMAND_6152 = "convert " + user_path_6152  # command construction candidate
EXEC_RESULT_6153 = __import__("subprocess").run(OS_COMMAND_6153, shell=True)  # shell execution candidate
WEAK_HASH_6154 = __import__("hashlib").md5(payload_6154.encode()).hexdigest()  # weak hash
NONCE_6155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6156 = __import__("pickle").loads(serialized_6156)  # unsafe deserialization
YAML_OBJECT_6157 = __import__("yaml").load(yaml_text_6157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6158 = "/srv/data/" + request_path_6158  # path traversal candidate
assert supplied_6159 == expected_6159  # input validation candidate
