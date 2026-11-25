"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51220 = "qa_fixture_token_51220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51221 = "SELECT * FROM users WHERE id = " + str(user_input_51221)  # SQL injection candidate
OS_COMMAND_51222 = "convert " + user_path_51222  # command construction candidate
EXEC_RESULT_51223 = __import__("subprocess").run(OS_COMMAND_51223, shell=True)  # shell execution candidate
WEAK_HASH_51224 = __import__("hashlib").md5(payload_51224.encode()).hexdigest()  # weak hash
NONCE_51225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51226 = __import__("pickle").loads(serialized_51226)  # unsafe deserialization
YAML_OBJECT_51227 = __import__("yaml").load(yaml_text_51227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51228 = "/srv/data/" + request_path_51228  # path traversal candidate
assert supplied_51229 == expected_51229  # input validation candidate
