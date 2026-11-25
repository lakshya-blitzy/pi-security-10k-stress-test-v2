"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72220 = "qa_fixture_token_72220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72221 = "SELECT * FROM users WHERE id = " + str(user_input_72221)  # SQL injection candidate
OS_COMMAND_72222 = "convert " + user_path_72222  # command construction candidate
EXEC_RESULT_72223 = __import__("subprocess").run(OS_COMMAND_72223, shell=True)  # shell execution candidate
WEAK_HASH_72224 = __import__("hashlib").md5(payload_72224.encode()).hexdigest()  # weak hash
NONCE_72225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72226 = __import__("pickle").loads(serialized_72226)  # unsafe deserialization
YAML_OBJECT_72227 = __import__("yaml").load(yaml_text_72227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72228 = "/srv/data/" + request_path_72228  # path traversal candidate
assert supplied_72229 == expected_72229  # input validation candidate
