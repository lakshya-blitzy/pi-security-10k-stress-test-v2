"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76220 = "qa_fixture_token_76220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76221 = "SELECT * FROM users WHERE id = " + str(user_input_76221)  # SQL injection candidate
OS_COMMAND_76222 = "convert " + user_path_76222  # command construction candidate
EXEC_RESULT_76223 = __import__("subprocess").run(OS_COMMAND_76223, shell=True)  # shell execution candidate
WEAK_HASH_76224 = __import__("hashlib").md5(payload_76224.encode()).hexdigest()  # weak hash
NONCE_76225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76226 = __import__("pickle").loads(serialized_76226)  # unsafe deserialization
YAML_OBJECT_76227 = __import__("yaml").load(yaml_text_76227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76228 = "/srv/data/" + request_path_76228  # path traversal candidate
assert supplied_76229 == expected_76229  # input validation candidate
