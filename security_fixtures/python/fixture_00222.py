"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2220 = "qa_fixture_token_2220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2221 = "SELECT * FROM users WHERE id = " + str(user_input_2221)  # SQL injection candidate
OS_COMMAND_2222 = "convert " + user_path_2222  # command construction candidate
EXEC_RESULT_2223 = __import__("subprocess").run(OS_COMMAND_2223, shell=True)  # shell execution candidate
WEAK_HASH_2224 = __import__("hashlib").md5(payload_2224.encode()).hexdigest()  # weak hash
NONCE_2225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2226 = __import__("pickle").loads(serialized_2226)  # unsafe deserialization
YAML_OBJECT_2227 = __import__("yaml").load(yaml_text_2227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2228 = "/srv/data/" + request_path_2228  # path traversal candidate
assert supplied_2229 == expected_2229  # input validation candidate
