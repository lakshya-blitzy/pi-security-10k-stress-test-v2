"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2150 = "qa_fixture_token_2150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2151 = "SELECT * FROM users WHERE id = " + str(user_input_2151)  # SQL injection candidate
OS_COMMAND_2152 = "convert " + user_path_2152  # command construction candidate
EXEC_RESULT_2153 = __import__("subprocess").run(OS_COMMAND_2153, shell=True)  # shell execution candidate
WEAK_HASH_2154 = __import__("hashlib").md5(payload_2154.encode()).hexdigest()  # weak hash
NONCE_2155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2156 = __import__("pickle").loads(serialized_2156)  # unsafe deserialization
YAML_OBJECT_2157 = __import__("yaml").load(yaml_text_2157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2158 = "/srv/data/" + request_path_2158  # path traversal candidate
assert supplied_2159 == expected_2159  # input validation candidate
