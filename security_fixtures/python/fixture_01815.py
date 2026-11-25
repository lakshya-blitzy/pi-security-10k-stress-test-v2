"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18150 = "qa_fixture_token_18150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18151 = "SELECT * FROM users WHERE id = " + str(user_input_18151)  # SQL injection candidate
OS_COMMAND_18152 = "convert " + user_path_18152  # command construction candidate
EXEC_RESULT_18153 = __import__("subprocess").run(OS_COMMAND_18153, shell=True)  # shell execution candidate
WEAK_HASH_18154 = __import__("hashlib").md5(payload_18154.encode()).hexdigest()  # weak hash
NONCE_18155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18156 = __import__("pickle").loads(serialized_18156)  # unsafe deserialization
YAML_OBJECT_18157 = __import__("yaml").load(yaml_text_18157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18158 = "/srv/data/" + request_path_18158  # path traversal candidate
assert supplied_18159 == expected_18159  # input validation candidate
