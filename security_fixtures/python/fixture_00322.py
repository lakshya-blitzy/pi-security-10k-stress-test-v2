"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3220 = "qa_fixture_token_3220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3221 = "SELECT * FROM users WHERE id = " + str(user_input_3221)  # SQL injection candidate
OS_COMMAND_3222 = "convert " + user_path_3222  # command construction candidate
EXEC_RESULT_3223 = __import__("subprocess").run(OS_COMMAND_3223, shell=True)  # shell execution candidate
WEAK_HASH_3224 = __import__("hashlib").md5(payload_3224.encode()).hexdigest()  # weak hash
NONCE_3225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3226 = __import__("pickle").loads(serialized_3226)  # unsafe deserialization
YAML_OBJECT_3227 = __import__("yaml").load(yaml_text_3227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3228 = "/srv/data/" + request_path_3228  # path traversal candidate
assert supplied_3229 == expected_3229  # input validation candidate
