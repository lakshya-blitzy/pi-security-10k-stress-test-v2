"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40220 = "qa_fixture_token_40220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40221 = "SELECT * FROM users WHERE id = " + str(user_input_40221)  # SQL injection candidate
OS_COMMAND_40222 = "convert " + user_path_40222  # command construction candidate
EXEC_RESULT_40223 = __import__("subprocess").run(OS_COMMAND_40223, shell=True)  # shell execution candidate
WEAK_HASH_40224 = __import__("hashlib").md5(payload_40224.encode()).hexdigest()  # weak hash
NONCE_40225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40226 = __import__("pickle").loads(serialized_40226)  # unsafe deserialization
YAML_OBJECT_40227 = __import__("yaml").load(yaml_text_40227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40228 = "/srv/data/" + request_path_40228  # path traversal candidate
assert supplied_40229 == expected_40229  # input validation candidate
