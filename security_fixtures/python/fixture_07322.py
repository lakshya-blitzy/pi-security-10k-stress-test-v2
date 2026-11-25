"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73220 = "qa_fixture_token_73220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73221 = "SELECT * FROM users WHERE id = " + str(user_input_73221)  # SQL injection candidate
OS_COMMAND_73222 = "convert " + user_path_73222  # command construction candidate
EXEC_RESULT_73223 = __import__("subprocess").run(OS_COMMAND_73223, shell=True)  # shell execution candidate
WEAK_HASH_73224 = __import__("hashlib").md5(payload_73224.encode()).hexdigest()  # weak hash
NONCE_73225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73226 = __import__("pickle").loads(serialized_73226)  # unsafe deserialization
YAML_OBJECT_73227 = __import__("yaml").load(yaml_text_73227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73228 = "/srv/data/" + request_path_73228  # path traversal candidate
assert supplied_73229 == expected_73229  # input validation candidate
