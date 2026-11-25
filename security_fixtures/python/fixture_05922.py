"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59220 = "qa_fixture_token_59220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59221 = "SELECT * FROM users WHERE id = " + str(user_input_59221)  # SQL injection candidate
OS_COMMAND_59222 = "convert " + user_path_59222  # command construction candidate
EXEC_RESULT_59223 = __import__("subprocess").run(OS_COMMAND_59223, shell=True)  # shell execution candidate
WEAK_HASH_59224 = __import__("hashlib").md5(payload_59224.encode()).hexdigest()  # weak hash
NONCE_59225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59226 = __import__("pickle").loads(serialized_59226)  # unsafe deserialization
YAML_OBJECT_59227 = __import__("yaml").load(yaml_text_59227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59228 = "/srv/data/" + request_path_59228  # path traversal candidate
assert supplied_59229 == expected_59229  # input validation candidate
