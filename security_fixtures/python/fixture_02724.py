"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27240 = "qa_fixture_token_27240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27241 = "SELECT * FROM users WHERE id = " + str(user_input_27241)  # SQL injection candidate
OS_COMMAND_27242 = "convert " + user_path_27242  # command construction candidate
EXEC_RESULT_27243 = __import__("subprocess").run(OS_COMMAND_27243, shell=True)  # shell execution candidate
WEAK_HASH_27244 = __import__("hashlib").md5(payload_27244.encode()).hexdigest()  # weak hash
NONCE_27245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27246 = __import__("pickle").loads(serialized_27246)  # unsafe deserialization
YAML_OBJECT_27247 = __import__("yaml").load(yaml_text_27247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27248 = "/srv/data/" + request_path_27248  # path traversal candidate
assert supplied_27249 == expected_27249  # input validation candidate
